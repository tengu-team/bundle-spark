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
import re
import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')
import requests
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, SparkSession
from pyspark.sql.functions import split

conf = SparkConf().setAppName('Write Data')
sc = SparkContext(conf=conf)
spark = SparkSession(sc)



file = requests.get('https://data.nasa.gov/resource/y77d-th95.csv')
f = re.sub("([a-z]+),", r"\1:", file.text)
data = sc.parallelize(f.splitlines())
rdd = data.map(lambda x: x.replace("\"","").split(","))
header = rdd.first()
df = rdd.filter(lambda row : row != header).toDF(header)
df.write.format('parquet').save('raw_data.parquet')
