import logging
from pathlib import Path

class LogGen:

    @staticmethod
    def loggen():

        log_path=Path(__file__).parent.parent.parent / "logs"
        log_path.mkdir(exist_ok=True)

        log_file=log_path/"automation.log"
        logging.basicConfig(filename=log_file,format=" %(asctime)s : %(levelname)s : %(message)s ",
                            level=logging.INFO,force=True,filemode="w")
        logger=logging.getLogger("GuviProject")
        return logger



