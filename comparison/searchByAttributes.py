    def searchByAttributes(self, jsonData, response):
        # type: (str,bytearray) -> int
        """ Find records matching the provided attributes
        Args:
            jsonData: A JSON document containing the attribute information to search.
            response: A bytearray for returning the response document; if an error occurred, an error response is stored here.
        """
        response[::] = b''
        _jsonData = self.prepareStringArgument(jsonData)
        responseBuf = c_char_p(addressof(tls_var.buf))
        responseSize = c_size_t(tls_var.bufSize)
        self._lib_handle.G2_searchByAttributes.argtypes = [c_char_p, POINTER(c_char_p), POINTER(c_size_t), self._resize_func_def]
        ret_code = self._lib_handle.G2_searchByAttributes(_jsonData, pointer(responseBuf), pointer(responseSize), self._resize_func)

        if ret_code == -1:
            raise G2ModuleNotInitialized('G2Engine has not been successfully initialized')
        elif ret_code < 0:
            self._lib_handle.G2_getLastException(tls_var.buf, sizeof(tls_var.buf))
            raise TranslateG2ModuleException(tls_var.buf.value)

        response += tls_var.buf.value
