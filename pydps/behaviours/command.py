# ------------------------------------------------------------------------------
#  MIT License
#
#  Copyright (c) 2021, Hieu Pham. All rights reserved.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# ------------------------------------------------------------------------------
from typing import Any
from abc import ABC, abstractmethod


class CommandInterface(ABC):
    """
    This is command interface declares a method for executing a command.
    ---------
    @author:    Hieu Pham.
    @created:   24-05-2021.
    @modified:  24-05-2021.
    """

    @abstractmethod
    def do(self) -> Any:
        """
        Perform the command.
        :return: anything.
        """
        pass

    @abstractmethod
    def undo(self) -> Any:
        """
        Undo the command.
        :return: anything.
        """
        pass
