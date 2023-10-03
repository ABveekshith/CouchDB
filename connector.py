from abc import ABCMeta, abstractmethod


class Connector(metaclass=ABCMeta):
    """
        this class should be inherited to every connector and should follow
        the methods that defined.
    """

    @abstractmethod
    def initialize(config: 'Config class') -> bool:
        """
        this method must implement the neccessary authorization
        for the connector and will be passed an instance of config class
        """
        pass

    @abstractmethod
    def start_poll() -> bool:
        """
        this method will implement data pulling from the
        source through the connector.

        this will use the json file mentioned in the config as the
        config for which all objects/entities to be fetched.
        """
        pass

    @abstractmethod
    def start_poll_batch() -> bool:
        """
        this method will implement data pulling from the
        source through the connector.

        this will use the json file mentioned in the config as the
        config for which all objects/entities to be fetched.
        """
        pass

    @classmethod
    def poll_status() -> str:
        """
        this method should return the status of the data transfer .
        Here are the list of status
            - accepted
            - inprogress
        """
        pass

    @classmethod
    def set_job_status(self, datasource_id: int, status: str) -> str:
        """
        the method should set the status for a job.
        """
        pass
        
