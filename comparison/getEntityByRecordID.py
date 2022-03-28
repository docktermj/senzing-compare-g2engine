    def getEntityByRecordID(self, dsrcCode, recordId, response):
        # type: (str,str,bytearray) -> int
        """ Get the entity containing the specified record
        Args:
            dataSourceCode: The data source for the observation.
            recordID: The ID for the record
            response: A bytearray for returning the response document; if an error occurred, an error response is stored here.
        """

        response[::] = b''
        _dsrcCode = self.prepareStringArgument(dsrcCode)
        _recordId = self.prepareStringArgument(recordId)
        responseBuf = c_char_p(addressof(tls_var.buf))
        responseSize = c_size_t(tls_var.bufSize)
        self._lib_handle.G2_getEntityByRecordID.argtypes = [c_char_p, c_char_p, POINTER(c_char_p), POINTER(c_size_t), self._resize_func_def]
        ret_code = self._lib_handle.G2_getEntityByRecordID(_dsrcCode, _recordId, pointer(responseBuf), pointer(responseSize), self._resize_func)

        if ret_code == -1:
            raise G2ModuleNotInitialized('G2Engine has not been successfully initialized')
        elif ret_code < 0:
            self._lib_handle.G2_getLastException(tls_var.buf, sizeof(tls_var.buf))
            raise TranslateG2ModuleException(tls_var.buf.value)

        response += tls_var.buf.value
