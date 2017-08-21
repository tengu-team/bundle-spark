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

conf = SparkConf().setAppName('Write Data').setMaster('local')
sc = SparkContext(conf=conf)

df = spark.read.parquet("data.parquet")
df_ver2 = df.filter(df['nametype'] == 'Valid').select(df['id'] + df['mass'] + df['name'] + df['year'] + df['recclass'] + df['reclat'] + df['reclong']).

df.write.format('parquet').save('valid_data.parquet')
