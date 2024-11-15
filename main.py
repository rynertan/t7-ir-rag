class PatentRAG:
    """
    PatentRAG is a class that handles the ingestion, indexing, and querying of
    patent data.

    Attributes:
      PERSIST_DIR (str): The directory where persistent storage is maintained.

    Methods:
      __init__():
        Initializes the PatentRAG instance.

      data_ingestion(dir: str):

      load_index(path: str):

      query(query: str):
    """

    PERSIST_DIR = "./storage"

    def __init__(self):
        pass

    def data_ingestion(self, dir: str):
        """
        Ingests data from the specified directory.
        Args:
          dir (str): The path to the directory containing the data to be
          ingested.
        Returns:
          None
        """

        pass

    def load_index(self, path: str):
        """
        Loads the index from the specified path.
        Args:
          path (str): The path to the index file.
        Returns:
          None
        """

        pass

    def query(self, query: str):
        """
        Queries the index for the specified query.
        Args:
          query (str): The query to be searched for.
        Returns:
          None
        """

        pass
