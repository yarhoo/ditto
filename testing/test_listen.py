# Copyright 2013 MemSQL, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

# Tests only the binlog listening part of ditto. It flushes the MySQL
# binlog, runs the .sql file on the MySQL side then runs
# test_replication.py to check the binlog replaying onto MemSQL.


import subprocess
from memsql import tools
from testing_globs import *
import logging

filepath, dbname, loglevel = setup_databases()

run_mysql(filepath, dbname)

# Runs test_replication
ditto_arglist = ["python", "../scripts/test_replication.py", dbname, "--no-dump",
                 "--no-blocking", "--resume-from-start", "--log="+loglevel]
logging.debug('executing: %s' % (' '.join(ditto_arglist)))
subprocess.call(ditto_arglist)
