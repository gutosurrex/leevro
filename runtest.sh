#! /bin/bash

source vir/bin/activate

py.test -s tests/

deactivate
