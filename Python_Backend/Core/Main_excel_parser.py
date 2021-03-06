import sys
import os
sys.path.append(os.path.join(os.getcwd(), "venv", "Lib", "site-packages"))

from Core.Logger import Logger
from Core.Validate import Validate_res
from Core.Query import Query_creator as qc
from Core.DAO import XML_DAO as xpc
from Core.Parser.Opt_parser import Opts as Opt
from Core.DAO.DB_connector import Connection as con
from PyQt5 import QtCore


class Opts:
    def __init__(self, mode):
        self.args = Args(mode)

class Args:
    def __init__(self, arg):
        self.test_mode = arg


class MainLoader(QtCore.QThread):
    pyqt_signal_debug = QtCore.pyqtSignal(str)
    pyqt_signal_log = QtCore.pyqtSignal(str)
    pyqt_signal_error = QtCore.pyqtSignal(str)
    pyqt_signal_message = QtCore.pyqtSignal()

    def __init__(self, path, mode, parent=None):
        super().__init__(parent)
        self.path = [path]
        self.opts = Opts(mode)

    @staticmethod
    def api_config(*path, opts):
        opts = Opts(opts)
        for pathToConfigXML in path:
            try:
                loggerInst = Logger.Log_info(
                    pathToConfigXML,
                    path
                )
                loggerInst.set_config(pathToConfigXML)
                loggerInst.raiseInfo(4)
                dbService = xpc.XmlParser.api_dict(pathToConfigXML, loggerInst, opts)
                return dbService
            except Exception as e:
                raise e

    def run(self):
        connector = None

        for pathToConfigXML in self.path:
            try:
                loggerInst = Logger.Log_info(
                    pathToConfigXML,
                    self.path,
                    signal_debug=self.pyqt_signal_debug,
                    signal_log=self.pyqt_signal_log,
                    signal_error=self.pyqt_signal_error
                )
                loggerInst.set_config(pathToConfigXML)
                loggerInst.raiseInfo(4)
                dbService = xpc.XmlParser(pathToConfigXML, loggerInst, self.opts)
                connector = con.get_instance(loggerInst)
            except Exception as e:
                self.pyqt_signal_error.emit(e.args[0])
                return
            try:
                connector.connectToTheDB(
                                         dbService.dictionary["dbHost"],
                                         dbService.dictionary["dbUser"],
                                         dbService.dictionary["dbPass"],
                                         dbService.dictionary["dbBase"],
                                         dbService.dictionary["dbPort"],
                                         dbService.dictionary["dbtype"])
            except Exception as e:
                self.pyqt_signal_error.emit(e.args[0])
                return

            validator = Validate_res.Validate(dbService, loggerInst, self.opts, connector)

            try:
                validator.validate()
            except Exception as e:
                self.pyqt_signal_error.emit(e.args[0])
                return

            if dbService.dictionary['checkMode_value'] == 'true':
                connector.closeConnect()
                loggerInst.raiseInfo(7)
                break

            try:
                queryService = qc.Query(dbService, loggerInst, self.opts, connector)
            except Exception as e:
                self.pyqt_signal_error.emit(e.args[0])
                return


            try:
                queryService.execAllQueries()
            except Exception as e:
                self.pyqt_signal_error.emit(f'Error at execution. Please check column configurations.\n---\n{e}')
                return
            loggerInst.raiseInfo(7)

        if connector:
            connector.closeConnect()


if __name__ == '__main__':

    opts = Opt()

    connector = None

    for pathToConfigXML in opts.args.config:
        loggerInst = Logger.Log_info.getInstance(pathToConfigXML, opts.args.config)
        loggerInst.set_config(pathToConfigXML)
        loggerInst.raiseInfo(4)
        dbService = xpc.XmlParser(pathToConfigXML, loggerInst, opts)

        connector = con.get_instance(loggerInst)
        connector.connectToTheDB(
            dbService.dictionary["dbHost"],
            dbService.dictionary["dbUser"],
            dbService.dictionary["dbPass"],
            dbService.dictionary["dbBase"],
            dbService.dictionary["dbPort"],
            dbService.dictionary["dbtype"])

        validator = Validate_res.Validate(dbService, loggerInst, opts, connector)
        validator.validate()

        if dbService.dictionary['checkMode_value'] == 'true':
            connector.closeConnect()
            loggerInst.raiseInfo(7)
            break

        queryService = qc.Query(dbService, loggerInst, opts, connector)
        queryService.execAllQueries()

        loggerInst.raiseInfo(7)

    if connector:
        connector.closeConnect()