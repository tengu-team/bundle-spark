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
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, SparkSession
from pyspark.sql.functions import split

conf = SparkConf().setAppName('Transform Data')
sc = SparkContext(conf=conf)
spark = SparkSession(sc)

df = spark.read.parquet("~/raw_data.parquet")
df_ver2 = df.filter(df['nametype'] == 'Valid').select(df['id'], df['mass'], df['name'], df['year'], df['recclass'], df['reclat'], df['reclong'])

df_ver2.write.format('parquet').save('~/valid_data.parquet')
