#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Descrition: Delet useless infomation in PNG
            删除png中辅助信息
'''

class InfoDelet(object):
    _SAVE_TYPE = ('IHDR', 'IDAT', 'IEND')
    def __init__(self):
        self._in_file = None
        self._out_file = None
        self._bytes_read = 0

    def setInFile(self, file_name):
        '''
        :param str fil_ename: the file is read
        :return : None 
        '''
        self._in_file = open(file_name, mode='rb+')

    def setOutFile(self, file_name):
        '''
        :param str file_name: the file to save
        '''
        self._out_file = open(file_name, mode='wb+')
        self._out_file.write(self._read_bytes(8))
        self._save_next_chunk()

    def _read_bytes(self, byte_count):
        self._bytes_read += byte_count
        return self._in_file.read(byte_count)


    def _save_next_chunk(self):
        chunk_size_str = self._read_bytes(4)
        chunk_size = int(chunk_size_str.encode('hex'), 16)
        chunk_type = self._read_bytes(4)
        content = self._read_bytes(chunk_size)
        crc = self._read_bytes(4)
        if chunk_type.encode('ascii') in self._SAVE_TYPE:
            self._out_file.write(chunk_size_str + chunk_type + content + crc)
        if not chunk_size:
            return
        self._save_next_chunk()


if __name__ == '__main__':
    infoDelet = InfoDelet()
    infoDelet.setInFile('./test.png')
    infoDelet.setOutFile('./new.png')




    