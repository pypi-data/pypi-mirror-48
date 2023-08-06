# @file DecParser.py
# Code to help parse DEC file
##
# Copyright (c) 2018, Microsoft Corporation
#
# All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
##
###
from MuPythonLibrary.Uefi.EdkII.Parsers.BaseParser import HashFileParser
import os


class DecParser(HashFileParser):
    def __init__(self):
        HashFileParser.__init__(self, 'DecParser')
        self.Lines = []
        self.Parsed = False
        self.Dict = {}
        self.LibrariesUsed = []
        self.PPIsUsed = []
        self.ProtocolsUsed = []
        self.GuidsUsed = []
        self.PcdsUsed = []
        self.IncludesUsed = []
        self.Path = ""

    def ParseFile(self, filepath):
        self.Logger.debug("Parsing file: %s" % filepath)
        if(not os.path.isabs(filepath)):
            fp = self.FindPath(filepath)
        else:
            fp = filepath
        self.Path = fp

        f = open(fp, "r")
        self.Lines = f.readlines()
        f.close()
        InDefinesSection = False
        InLibraryClassSection = False
        InProtocolsSection = False
        InGuidsSection = False
        InPPISection = False
        InPcdSection = False
        InIncludesSection = False

        for line in self.Lines:
            sline = self.StripComment(line)

            if(sline is None or len(sline) < 1):
                continue

            if InDefinesSection:
                if sline.strip()[0] == '[':
                    InDefinesSection = False
                else:
                    if sline.count("=") == 1:
                        tokens = sline.split('=', 1)
                        self.Dict[tokens[0].strip()] = tokens[1].strip()
                        continue

            elif InLibraryClassSection:
                if sline.strip()[0] == '[':
                    InLibraryClassSection = False
                else:
                    t = sline.partition("|")
                    self.LibrariesUsed.append(t[0].strip())
                    continue

            elif InProtocolsSection:
                if sline.strip()[0] == '[':
                    InProtocolsSection = False
                else:
                    t = sline.partition("=")
                    self.ProtocolsUsed.append(t[0].strip())
                    continue

            elif InGuidsSection:
                if sline.strip()[0] == '[':
                    InGuidsSection = False
                else:
                    t = sline.partition("=")
                    self.GuidsUsed.append(t[0].strip())
                    continue

            elif InPcdSection:
                if sline.strip()[0] == '[':
                    InPcdSection = False
                else:
                    t = sline.partition("|")
                    self.PcdsUsed.append(t[0].strip())
                    continue

            elif InIncludesSection:
                if sline.strip()[0] == '[':
                    InIncludesSection = False
                else:
                    self.IncludesUsed.append(sline.strip())
                    continue

            elif InPPISection:
                if (sline.strip()[0] == '['):
                    InPPISection = False
                else:
                    t = sline.partition("=")
                    self.PPIsUsed.append(t[0].strip())
                    continue

            # check for different sections
            if sline.strip().lower().startswith('[defines'):
                InDefinesSection = True

            elif sline.strip().lower().startswith('[libraryclasses'):
                InLibraryClassSection = True

            elif sline.strip().lower().startswith('[protocols'):
                InProtocolsSection = True

            elif sline.strip().lower().startswith('[guids'):
                InGuidsSection = True

            elif sline.strip().lower().startswith('[ppis'):
                InPPISection = True

            elif sline.strip().lower().startswith('[pcd'):
                InPcdSection = True

            elif sline.strip().lower().startswith('[includes'):
                InIncludesSection = True

        self.Parsed = True
