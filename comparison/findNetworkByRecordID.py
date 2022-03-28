    def findNetworkByRecordID(self, recordList, maxDegree, buildOutDegree, maxEntities, response):
        # type: (str,str) -> str
        """ Find a network between entities in the system.
        Args:
            recordList: The records to search for the network of
            maxDegree: The maximum path length to search for between entities
            buildOutDegree: The number of degrees to build out the surrounding network
            maxEntities: The maximum number of entities to include in the result
            response: A bytearray for returning the response document.
        """

        response[::] = b''
        _recordList = self.prepareStringArgument(recordList)
        responseBuf = c_char_p(addressof(tls_var.buf))
        responseSize = c_size_t(tls_var.bufSize)
        self._lib_handle.G2_findNetworkByRecordID.restype = c_int
        self._lib_handle.G2_findNetworkByRecordID.argtypes = [c_char_p, c_int, c_int, c_int, POINTER(c_char_p), POINTER(c_size_t), self._resize_func_def]
        ret_code = self._lib_handle.G2_findNetworkByRecordID(_recordList, maxDegree, buildOutDegree, maxEntities, pointer(responseBuf), pointer(responseSize), self._resize_func)
        if ret_code == -1:
            raise G2ModuleNotInitialized('G2Engine has not been successfully initialized')
        elif ret_code < 0:
            self._lib_handle.G2_getLastException(tls_var.buf, sizeof(tls_var.buf))
            raise TranslateG2ModuleException(tls_var.buf.value)

        response += tls_var.buf.value
