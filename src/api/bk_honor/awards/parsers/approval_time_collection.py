"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
from dataclasses import dataclass

from bk_honor.awards.constants import StepType

from . import register_parser, register_policy
from .collection import Collection, CollectionPolicy


@dataclass
class ApprovalTimeCollection(Collection):
    """审批时间收集步骤解析器"""


register_parser(StepType.APPROVAL_TIME_COLLECTION.value, ApprovalTimeCollection)
register_policy(StepType.APPROVAL_TIME_COLLECTION.value, CollectionPolicy)
