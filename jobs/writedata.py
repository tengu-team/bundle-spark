#!/usr/bin/env python3
# Copyright (C) 2017  Qrama
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# pylint: disable=c0111,c0103,c0301,c0412
import subprocess
import tempfile
from pyspark import SparkContext, SparkConf
from pyspark.sql.functions import split

conf = SparkConf().setAppName('Write Data').setMaster('local')
sc = SparkContext(conf=conf)

job_dir = '/tmp'
subprocess.check_call(['wget', '--output-document={}/data.csv'.format(job_dir),
                       'http://www.sharecsv.com/dl/4165c9b03d9fffdef43a3226613ff37c/Countries.csv'])
f=open("{}/data.csv".format(job_dir)).read()
data = sc.parallelize(f)
data_rdd = data.map(lambda line: line.split(','))

data_rdd.saveAsTextFile('/user/root/data/data2.csv')
