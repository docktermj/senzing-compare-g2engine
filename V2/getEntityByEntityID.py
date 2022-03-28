    def getEntityByEntityIDV2(self, entityID, flags, response):
        # type: (int,bytearray) -> int
        """ Find the entity with the given ID
        Args:
            entityID: The entity ID you want returned.  Typically referred to as
                      ENTITY_ID in JSON results.
            flags: control flags.
            response: A bytearray for returning the response document; if an error occurred, an error response is stored here.
        """

        response[::] = b''
        responseBuf = c_char_p(addressof(tls_var.buf))
        responseSize = c_size_t(tls_var.bufSize)
        self._lib_handle.G2_getEntityByEntityID_V2.restype = c_int
        self._lib_handle.G2_getEntityByEntityID_V2.argtypes = [c_longlong, c_longlong, POINTER(c_char_p), POINTER(c_size_t), self._resize_func_def]
        ret_code = self._lib_handle.G2_getEntityByEntityID_V2(entityID, flags, pointer(responseBuf), pointer(responseSize), self._resize_func)

        if ret_code == -1:
            raise G2ModuleNotInitialized('G2Engine has not been successfully initialized')
        elif ret_code < 0:
            self._lib_handle.G2_getLastException(tls_var.buf, sizeof(tls_var.buf))
            raise TranslateG2ModuleException(tls_var.buf.value)

        # Add the bytes to the response bytearray from calling function
        response += tls_var.buf.value
