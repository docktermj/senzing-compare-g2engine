    def findNetworkByEntityIDV2(self, entityList, maxDegree, buildOutDegree, maxEntities, flags, response):
        # type: (int) -> str
        """ Find a network between entities in the system.
        Args:
            entityList: The entities to search for the network of
            maxDegree: The maximum path length to search for between entities
            buildOutDegree: The number of degrees to build out the surrounding network
            maxEntities: The maximum number of entities to include in the result
            flags: control flags.
            response: A bytearray for returning the response document.
        """

        response[::] = b''
        _entityList = self.prepareStringArgument(entityList)
        responseBuf = c_char_p(addressof(tls_var.buf))
        responseSize = c_size_t(tls_var.bufSize)
        self._lib_handle.G2_findNetworkByEntityID_V2.restype = c_int
        self._lib_handle.G2_findNetworkByEntityID_V2.argtypes = [c_char_p, c_int, c_int, c_int, c_longlong, POINTER(c_char_p), POINTER(c_size_t), self._resize_func_def]
        ret_code = self._lib_handle.G2_findNetworkByEntityID_V2(_entityList, maxDegree, buildOutDegree, maxEntities, flags, pointer(responseBuf), pointer(responseSize), self._resize_func)
        if ret_code == -1:
            raise G2ModuleNotInitialized('G2Engine has not been successfully initialized')
        elif ret_code < 0:
            self._lib_handle.G2_getLastException(tls_var.buf, sizeof(tls_var.buf))
            raise TranslateG2ModuleException(tls_var.buf.value)

        response += tls_var.buf.value
