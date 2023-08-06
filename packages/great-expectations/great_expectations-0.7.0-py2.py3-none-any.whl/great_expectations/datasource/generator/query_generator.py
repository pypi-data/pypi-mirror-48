import os
import logging
import time

from .batch_generator import BatchGenerator

logger = logging.getLogger(__name__)

try:
    import sqlalchemy
    from sqlalchemy import create_engine, MetaData
except ImportError:
    sqlalchemy = None
    create_engine = None
    MetaData = None
    logger.debug("Unable to import sqlalchemy.")


class QueryGenerator(BatchGenerator):
    """Produce query-style batch_kwargs from sql files stored on disk
    """

    def __init__(self, datasource, name="default"):
        # TODO: Add tests for QueryGenerator
        super(QueryGenerator, self).__init__(name=name, type_="queries", datasource=datasource)
        self.meta = MetaData()
        if datasource is not None and datasource.data_context is not None:
            self._queries_path = os.path.join(self._datasource.data_context.root_directory,
                                              "datasources",
                                              self._datasource.name,
                                              "generators",
                                              self._name,
                                              "queries")
        else:
            self._queries_path = None
            self._queries = {}

        if datasource is not None:
            self.engine = datasource.engine

    def _get_iterator(self, data_asset_name, **kwargs):
        if self._queries_path:
            if data_asset_name in [path[:-4] for path in os.listdir(self._queries_path) if str(path).endswith(".sql")]:
                with open(os.path.join(self._queries_path, data_asset_name) + ".sql", "r") as data:
                    return iter([{
                        "query": data.read(),
                        "timestamp": time.time()
                    }])
        else:
            if data_asset_name in self._queries:
                return iter([{
                    "query": self._queries[data_asset_name],
                    "timestamp": time.time()
                }])

        if self.engine is not None:
            self.meta.reflect(bind=self.engine)
            tables = [str(table) for table in self.meta.sorted_tables]
            if data_asset_name in tables:
                return iter([
                    {
                        "table": data_asset_name,
                        "timestamp": time.time()
                    }
                ])

    def add_query(self, data_asset_name, query):
        if self._queries_path:
            with open(os.path.join(self._queries_path, data_asset_name + ".sql"), "w") as queryfile:
                queryfile.write(query)
        else:
            logger.info("Adding query to temporary storage only.")
            self._queries[data_asset_name] = query

    def get_available_data_asset_names(self):
        if self._queries_path:
            defined_queries = [path for path in os.walk(self._queries_path) if str(path).endswith(".sql")]
        else:
            defined_queries = list(self._queries.keys())
        if self.engine is not None:
            self.meta.reflect(bind=self.engine)
            tables = [str(table) for table in self.meta.sorted_tables]
        else:
            tables = []

        return set(defined_queries + tables)
