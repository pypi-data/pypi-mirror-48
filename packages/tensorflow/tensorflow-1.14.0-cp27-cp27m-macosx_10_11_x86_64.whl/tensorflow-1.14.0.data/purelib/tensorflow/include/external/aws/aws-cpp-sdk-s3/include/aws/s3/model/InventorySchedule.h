﻿/*
* Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
*
* Licensed under the Apache License, Version 2.0 (the "License").
* You may not use this file except in compliance with the License.
* A copy of the License is located at
*
*  http://aws.amazon.com/apache2.0
*
* or in the "license" file accompanying this file. This file is distributed
* on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
* express or implied. See the License for the specific language governing
* permissions and limitations under the License.
*/

#pragma once
#include <aws/s3/S3_EXPORTS.h>
#include <aws/s3/model/InventoryFrequency.h>
#include <utility>

namespace Aws
{
namespace Utils
{
namespace Xml
{
  class XmlNode;
} // namespace Xml
} // namespace Utils
namespace S3
{
namespace Model
{

  class AWS_S3_API InventorySchedule
  {
  public:
    InventorySchedule();
    InventorySchedule(const Aws::Utils::Xml::XmlNode& xmlNode);
    InventorySchedule& operator=(const Aws::Utils::Xml::XmlNode& xmlNode);

    void AddToNode(Aws::Utils::Xml::XmlNode& parentNode) const;


    /**
     * <p>Specifies how frequently inventory results are produced.</p>
     */
    inline const InventoryFrequency& GetFrequency() const{ return m_frequency; }

    /**
     * <p>Specifies how frequently inventory results are produced.</p>
     */
    inline void SetFrequency(const InventoryFrequency& value) { m_frequencyHasBeenSet = true; m_frequency = value; }

    /**
     * <p>Specifies how frequently inventory results are produced.</p>
     */
    inline void SetFrequency(InventoryFrequency&& value) { m_frequencyHasBeenSet = true; m_frequency = std::move(value); }

    /**
     * <p>Specifies how frequently inventory results are produced.</p>
     */
    inline InventorySchedule& WithFrequency(const InventoryFrequency& value) { SetFrequency(value); return *this;}

    /**
     * <p>Specifies how frequently inventory results are produced.</p>
     */
    inline InventorySchedule& WithFrequency(InventoryFrequency&& value) { SetFrequency(std::move(value)); return *this;}

  private:

    InventoryFrequency m_frequency;
    bool m_frequencyHasBeenSet;
  };

} // namespace Model
} // namespace S3
} // namespace Aws
