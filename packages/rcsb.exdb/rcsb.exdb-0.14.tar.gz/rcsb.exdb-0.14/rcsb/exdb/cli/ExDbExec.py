##
# File: ExDbExec.py
# Date: 22-Apr-2019  jdw
#
#  Execution wrapper  --  for extract and load operations -
#
#  Updates:
#
##
__docformat__ = "restructuredtext en"
__author__ = "John Westbrook"
__email__ = "jwest@rcsb.rutgers.edu"
__license__ = "Apache 2.0"

import argparse
import logging
import os
import sys

from rcsb.db.mongo.DocumentLoader import DocumentLoader

# from rcsb.db.scripts.ChemRefEtlWorker import ChemRefEtlWorker
# from rcsb.db.scripts.RepoHoldingsEtlWorker import RepoHoldingsEtlWorker
# from rcsb.db.scripts.SequenceClustersEtlWorker import SequenceClustersEtlWorker
from rcsb.exdb.cli.TreeNodeListWorker import TreeNodeListWorker
from rcsb.db.utils.TimeUtil import TimeUtil
from rcsb.utils.config.ConfigUtil import ConfigUtil

HERE = os.path.abspath(os.path.dirname(__file__))
TOPDIR = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]-%(module)s.%(funcName)s: %(message)s")
logger = logging.getLogger()


def loadStatus(statusList, cfgOb, readBackCheck=True):
    sectionName = "data_exchange"
    dl = DocumentLoader(cfgOb, "MONGO_DB", numProc=2, chunkSize=2, documentLimit=None, verbose=False, readBackCheck=readBackCheck)
    #
    databaseName = cfgOb.get("DATABASE_NAME", sectionName=sectionName)
    collectionName = cfgOb.get("COLLECTION_UPDATE_STATUS", sectionName=sectionName)
    ok = dl.load(databaseName, collectionName, loadType="append", documentList=statusList, indexAttributeList=["update_id", "database_name", "object_name"], keyNames=None)
    return ok


def main():
    parser = argparse.ArgumentParser()
    #
    defaultConfigName = "site_info"
    #
    parser.add_argument("--full", default=True, action="store_true", help="Fresh full load in a new tables/collections (Default)")
    #
    # parser.add_argument("--etl_entity_sequence_clusters", default=False, action='store_true', help="ETL entity sequence clusters")
    # parser.add_argument("--etl_repository_holdings", default=False, action='store_true', help="ETL repository holdings")
    # parser.add_argument("--etl_chemref", default=False, action='store_true', help="ETL integrated chemical reference data")
    parser.add_argument("--etl_tree_node_lists", default=False, action="store_true", help="ETL tree node lists")

    # parser.add_argument("--data_set_id", default=None, help="Data set identifier (default= 2018_14 for current week)")
    #
    # parser.add_argument("--sequence_cluster_data_path", default=None, help="Sequence cluster data path (default set by configuration")
    # parser.add_argument("--sandbox_data_path", default=None, help="Date exchange sandboxPath data path (default set by configuration")

    #
    parser.add_argument("--config_path", default=None, help="Path to configuration options file")
    parser.add_argument("--config_name", default=defaultConfigName, help="Configuration section name")

    parser.add_argument("--db_type", default="mongo", help="Database server type (default=mongo)")

    # parser.add_argument("--document_style", default="rowwise_by_name_with_cardinality",
    #                    help="Document organization (rowwise_by_name_with_cardinality|rowwise_by_name|columnwise_by_name|rowwise_by_id|rowwise_no_name")
    parser.add_argument("--read_back_check", default=False, action="store_true", help="Perform read back check on all documents")
    #
    parser.add_argument("--num_proc", default=2, help="Number of processes to execute (default=2)")
    parser.add_argument("--chunk_size", default=10, help="Number of files loaded per process")
    parser.add_argument("--document_limit", default=None, help="Load document limit for testing")
    parser.add_argument("--prune_document_size", default=None, help="Prune large documents to this size limit (MB)")
    parser.add_argument("--debug", default=False, action="store_true", help="Turn on verbose logging")
    parser.add_argument("--mock", default=False, action="store_true", help="Use MOCK repository configuration for testing")
    # parser.add_argument("--working_path", default=None, help="Working path for temporary files")
    parser.add_argument("--top_cache_path", default=None, help="Top cache path for external and local resource files")
    parser.add_argument("--use_cache", default=False, action="store_true", help="Use cache files from remote resources")
    #
    #
    args = parser.parse_args()
    #
    debugFlag = args.debug
    if debugFlag:
        logger.setLevel(logging.DEBUG)
    # ----------------------- - ----------------------- - ----------------------- - ----------------------- - ----------------------- -
    #                                       Configuration Details
    configPath = args.config_path
    configName = args.config_name
    useCache = args.use_cache
    if not configPath:
        configPath = os.getenv("DBLOAD_CONFIG_PATH", None)
    try:
        if os.access(configPath, os.R_OK):
            os.environ["DBLOAD_CONFIG_PATH"] = configPath
            logger.info("Using configuation path %s (%s)", configPath, configName)
        else:
            logger.error("Missing or access issue with config file %r", configPath)
            exit(1)
        mockTopPath = os.path.join(TOPDIR, "rcsb", "mock-data") if args.mock else None
        cfgOb = ConfigUtil(configPath=configPath, defaultSectionName=defaultConfigName, mockTopPath=mockTopPath)
        if configName != defaultConfigName:
            cfgOb.replaceSectionName(defaultConfigName, configName)
        #
    except Exception as e:
        logger.error("Missing or access issue with config file %r with %s", configPath, str(e))
        exit(1)

    #
    try:
        readBackCheck = args.read_back_check
        tU = TimeUtil()
        dataSetId = args.data_set_id if args.data_set_id else tU.getCurrentWeekSignature()
        # seqDataLocator = args.sequence_cluster_data_path if args.sequence_cluster_data_path else cfgOb.getPath('RCSB_SEQUENCE_CLUSTER_DATA_PATH', sectionName=configName)
        # sandboxPath = args.sandbox_data_path if args.sandbox_data_path else cfgOb.getPath('RCSB_EXCHANGE_SANDBOX_PATH', sectionName=configName)
        numProc = int(args.num_proc)
        chunkSize = int(args.chunk_size)
        documentLimit = int(args.document_limit) if args.document_limit else None

        loadType = "full" if args.full else "replace"
        # loadType = 'replace' if args.replace else 'full'

        # workPath = args.working_path if args.working_path else "."
        topCachePath = args.top_cache_path if args.top_cache_path else "."

        # if args.document_style not in ['rowwise_by_name', 'rowwise_by_name_with_cardinality', 'columnwise_by_name', 'rowwise_by_id', 'rowwise_no_name']:
        #    logger.error("Unsupported document style %s" % args.document_style)

        if args.db_type != "mongo":
            logger.error("Unsupported database server type %s", args.db_type)
    except Exception as e:
        logger.exception("Argument processing problem %s", str(e))
        parser.print_help(sys.stderr)
        exit(1)
    # ----------------------- - ----------------------- - ----------------------- - ----------------------- - ----------------------- -
    ##
    if args.db_type == "mongo":
        if args.etl_tree_node_lists:
            rhw = TreeNodeListWorker(
                cfgOb,
                mockTopPath=mockTopPath,
                numProc=numProc,
                chunkSize=chunkSize,
                documentLimit=documentLimit,
                verbose=debugFlag,
                readBackCheck=readBackCheck,
                topCachePath=topCachePath,
                useCache=useCache,
            )
            ok = rhw.load(dataSetId, loadType=loadType)
            okS = loadStatus(rhw.getLoadStatus(), cfgOb, readBackCheck=readBackCheck)
        logger.info("Operation completed with status %r " % ok and okS)


if __name__ == "__main__":
    main()
