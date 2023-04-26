from flask import Flask
from multiprocessing import Process, Manager
from time import sleep
import ijson
import json
from sim_logging import get_logger
import ctypes
import os

logger = get_logger()

class Data:
    def __init__(self) -> None:
        self.init_data = {"data": None}
        self.data = Manager().Value(object, self.init_data)
        self.stop_sig = Manager().Value(ctypes.c_bool, False)
    
    def start(self):
        self.proc = Process(target=self._start_process, daemon=True)
        self.proc.start()

    def _start_process(self):
        log_name = os.environ.get("LOG_NAME", "log1681421163.731945.log")
        mnt_dir = os.environ.get("MNT_DIR", ".")
        path_to_file = os.path.join(mnt_dir, log_name)
        logger.info(f"Reading from file: {path_to_file}")
        try:
            stream_env = os.environ.get("STREAM_DATA", "False")
            stream_flag = stream_env.lower in ("true", "1", "t") # Allow values like True, true, 1, ...
            open_mode = "rb" if stream_flag else "r"
            with open(path_to_file, open_mode) as f:
                if not stream_flag:
                    logger.info("start parsing file")
                _data = ijson.items(f, "data.item") if stream_flag else json.load(f)
                if not stream_flag:
                    logger.info("done parsing file")
                for data in _data:
                    self.data.set(data)
                    sleep(1)
                    if self.stop_sig.value:
                        logger.info("stopped")
                        break
        except Exception as e:
            logger.info(e)
            return -1
        self.stop_sig.set(False)
        return 0

    def get_data(self):
        return self.data.value
    
    def stop(self):
        self.stop_sig.set(True)
        self.data.set(self.init_data)

app = Flask(__name__)

@app.route("/")
def main():
    return data.get_data()

@app.route("/start")
def start_process():
    data.start()
    return {"status": 1}

@app.route("/stop")
def stop_proc():
    data.stop()
    return {"status": 0}

if __name__ == '__main__':
    data = Data()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))