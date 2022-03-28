    def getVirtualEntityByRecordIDV2(self, recordList, flags, response):

        response[::] = b''
        _recordList = self.prepareStringArgument(recordList)
        responseBuf = c_char_p(addressof(tls_var.buf))
        responseSize = c_size_t(tls_var.bufSize)
        self._lib_handle.G2_getVirtualEntityByRecordID_V2.restype = c_int
        self._lib_handle.G2_getVirtualEntityByRecordID_V2.argtypes = [c_char_p, c_longlong, POINTER(c_char_p), POINTER(c_size_t), self._resize_func_def]
        ret_code = self._lib_handle.G2_getVirtualEntityByRecordID_V2(_recordList, flags, pointer(responseBuf), pointer(responseSize), self._resize_func)

        if ret_code == -1:
            raise G2ModuleNotInitialized('G2Engine has not been successfully initialized')
        elif ret_code < 0:
            self._lib_handle.G2_getLastException(tls_var.buf, sizeof(tls_var.buf))
            raise TranslateG2ModuleException(tls_var.buf.value)

        response += tls_var.buf.value
