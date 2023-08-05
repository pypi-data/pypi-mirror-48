# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RoaRequest
class ModifyDataSourceRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Airec', '2018-10-12', 'ModifyDataSource','airec')
		self.set_uri_pattern('/openapi/instances/[InstanceId]/dataSources/[TableName]')
		self.set_method('PUT')

	def get_InstanceId(self):
		return self.get_path_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_path_param('InstanceId',InstanceId)

	def get_TableName(self):
		return self.get_path_params().get('TableName')

	def set_TableName(self,TableName):
		self.add_path_param('TableName',TableName)