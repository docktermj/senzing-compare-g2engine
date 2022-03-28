    def findPathByEntityIDV2(self, startEntityID, endEntityID, maxDegree, flags, response):
        # type: (int) -> str
        """ Find a path between two entities in the system.
        Args:
            startEntityID: The entity ID you want to find the path from
            endEntityID: The entity ID you want to find the path to
            maxDegree: The maximum path length to search for
            flags: control flags.
            response: A bytearray for returning the response document.
        """

        response[::] = b''
        responseBuf = c_char_p(addressof(tls_var.buf))
        responseSize = c_size_t(tls_var.bufSize)
        self._lib_handle.G2_findPathByEntityID_V2.restype = c_int
        self._lib_handle.G2_findPathByEntityID_V2.argtypes = [c_longlong, c_longlong, c_int, c_longlong, POINTER(c_char_p), POINTER(c_size_t), self._resize_func_def]
        ret_code = self._lib_handle.G2_findPathByEntityID_V2(startEntityID, endEntityID, maxDegree, flags, pointer(responseBuf), pointer(responseSize), self._resize_func)
        if ret_code == -1:
            raise G2ModuleNotInitialized('G2Engine has not been successfully initialized')
        elif ret_code < 0:
            self._lib_handle.G2_getLastException(tls_var.buf, sizeof(tls_var.buf))
            raise TranslateG2ModuleException(tls_var.buf.value)

        response += tls_var.buf.value
