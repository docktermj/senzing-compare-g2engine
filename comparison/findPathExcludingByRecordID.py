    def findPathExcludingByRecordID(self, startDsrcCode, startRecordId, endDsrcCode, endRecordId, maxDegree, excludedEntities, response):
        # type: (str,str) -> str
        """ Find a path between two records in the system.
        Args:
            startDataSourceCode: The data source for the record you want to find the path from
            startRecordID: The ID for the record you want to find the path from
            endDataSourceCode: The data source for the record you want to find the path to
            endRecordID: The ID for the record you want to find the path to
            maxDegree: The maximum path length to search for
            excludedEntities: JSON document containing entities to exclude
            response: A bytearray for returning the response document.
        """

        response[::] = b''
        _startDsrcCode = self.prepareStringArgument(startDsrcCode)
        _startRecordId = self.prepareStringArgument(startRecordId)
        _endDsrcCode = self.prepareStringArgument(endDsrcCode)
        _endRecordId = self.prepareStringArgument(endRecordId)
        _excludedEntities = self.prepareStringArgument(excludedEntities)
        responseBuf = c_char_p(addressof(tls_var.buf))
        responseSize = c_size_t(tls_var.bufSize)
        self._lib_handle.G2_findPathExcludingByRecordID.restype = c_int
        self._lib_handle.G2_findPathExcludingByRecordID.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, c_int, c_char_p, POINTER(c_char_p), POINTER(c_size_t), self._resize_func_def]
        ret_code = self._lib_handle.G2_findPathExcludingByRecordID(_startDsrcCode, _startRecordId, _endDsrcCode, _endRecordId, maxDegree, _excludedEntities, pointer(responseBuf), pointer(responseSize), self._resize_func)

        if ret_code == -1:
            raise G2ModuleNotInitialized('G2Engine has not been successfully initialized')
        elif ret_code < 0:
            self._lib_handle.G2_getLastException(tls_var.buf, sizeof(tls_var.buf))
            raise TranslateG2ModuleException(tls_var.buf.value)

        response += tls_var.buf.value
