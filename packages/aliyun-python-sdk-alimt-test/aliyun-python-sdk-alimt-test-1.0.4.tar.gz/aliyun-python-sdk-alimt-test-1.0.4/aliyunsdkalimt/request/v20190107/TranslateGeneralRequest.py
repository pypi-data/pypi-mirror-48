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

from aliyunsdkcore.request import RpcRequest
class TranslateGeneralRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'alimt', '2019-01-07', 'TranslateGeneral','alimt')

	def get_SourceLanguage(self):
		return self.get_query_params().get('SourceLanguage')

	def set_SourceLanguage(self,SourceLanguage):
		self.add_query_param('SourceLanguage',SourceLanguage)

	def get_SourceText(self):
		return self.get_query_params().get('SourceText')

	def set_SourceText(self,SourceText):
		self.add_query_param('SourceText',SourceText)

	def get_FormatType(self):
		return self.get_query_params().get('FormatType')

	def set_FormatType(self,FormatType):
		self.add_query_param('FormatType',FormatType)

	def get_TargetLanguage(self):
		return self.get_query_params().get('TargetLanguage')

	def set_TargetLanguage(self,TargetLanguage):
		self.add_query_param('TargetLanguage',TargetLanguage)

	def get_Scene(self):
		return self.get_query_params().get('Scene')

	def set_Scene(self,Scene):
		self.add_query_param('Scene',Scene)