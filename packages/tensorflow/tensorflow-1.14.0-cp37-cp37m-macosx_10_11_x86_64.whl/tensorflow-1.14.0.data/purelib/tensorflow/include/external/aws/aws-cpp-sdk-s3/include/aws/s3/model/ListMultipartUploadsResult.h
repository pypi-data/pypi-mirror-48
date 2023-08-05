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
#include <aws/core/utils/memory/stl/AWSString.h>
#include <aws/core/utils/memory/stl/AWSVector.h>
#include <aws/s3/model/EncodingType.h>
#include <aws/s3/model/MultipartUpload.h>
#include <aws/s3/model/CommonPrefix.h>
#include <utility>

namespace Aws
{
template<typename RESULT_TYPE>
class AmazonWebServiceResult;

namespace Utils
{
namespace Xml
{
  class XmlDocument;
} // namespace Xml
} // namespace Utils
namespace S3
{
namespace Model
{
  class AWS_S3_API ListMultipartUploadsResult
  {
  public:
    ListMultipartUploadsResult();
    ListMultipartUploadsResult(const Aws::AmazonWebServiceResult<Aws::Utils::Xml::XmlDocument>& result);
    ListMultipartUploadsResult& operator=(const Aws::AmazonWebServiceResult<Aws::Utils::Xml::XmlDocument>& result);


    /**
     * <p>Name of the bucket to which the multipart upload was initiated.</p>
     */
    inline const Aws::String& GetBucket() const{ return m_bucket; }

    /**
     * <p>Name of the bucket to which the multipart upload was initiated.</p>
     */
    inline void SetBucket(const Aws::String& value) { m_bucket = value; }

    /**
     * <p>Name of the bucket to which the multipart upload was initiated.</p>
     */
    inline void SetBucket(Aws::String&& value) { m_bucket = std::move(value); }

    /**
     * <p>Name of the bucket to which the multipart upload was initiated.</p>
     */
    inline void SetBucket(const char* value) { m_bucket.assign(value); }

    /**
     * <p>Name of the bucket to which the multipart upload was initiated.</p>
     */
    inline ListMultipartUploadsResult& WithBucket(const Aws::String& value) { SetBucket(value); return *this;}

    /**
     * <p>Name of the bucket to which the multipart upload was initiated.</p>
     */
    inline ListMultipartUploadsResult& WithBucket(Aws::String&& value) { SetBucket(std::move(value)); return *this;}

    /**
     * <p>Name of the bucket to which the multipart upload was initiated.</p>
     */
    inline ListMultipartUploadsResult& WithBucket(const char* value) { SetBucket(value); return *this;}


    /**
     * <p>The key at or after which the listing began.</p>
     */
    inline const Aws::String& GetKeyMarker() const{ return m_keyMarker; }

    /**
     * <p>The key at or after which the listing began.</p>
     */
    inline void SetKeyMarker(const Aws::String& value) { m_keyMarker = value; }

    /**
     * <p>The key at or after which the listing began.</p>
     */
    inline void SetKeyMarker(Aws::String&& value) { m_keyMarker = std::move(value); }

    /**
     * <p>The key at or after which the listing began.</p>
     */
    inline void SetKeyMarker(const char* value) { m_keyMarker.assign(value); }

    /**
     * <p>The key at or after which the listing began.</p>
     */
    inline ListMultipartUploadsResult& WithKeyMarker(const Aws::String& value) { SetKeyMarker(value); return *this;}

    /**
     * <p>The key at or after which the listing began.</p>
     */
    inline ListMultipartUploadsResult& WithKeyMarker(Aws::String&& value) { SetKeyMarker(std::move(value)); return *this;}

    /**
     * <p>The key at or after which the listing began.</p>
     */
    inline ListMultipartUploadsResult& WithKeyMarker(const char* value) { SetKeyMarker(value); return *this;}


    /**
     * <p>Upload ID after which listing began.</p>
     */
    inline const Aws::String& GetUploadIdMarker() const{ return m_uploadIdMarker; }

    /**
     * <p>Upload ID after which listing began.</p>
     */
    inline void SetUploadIdMarker(const Aws::String& value) { m_uploadIdMarker = value; }

    /**
     * <p>Upload ID after which listing began.</p>
     */
    inline void SetUploadIdMarker(Aws::String&& value) { m_uploadIdMarker = std::move(value); }

    /**
     * <p>Upload ID after which listing began.</p>
     */
    inline void SetUploadIdMarker(const char* value) { m_uploadIdMarker.assign(value); }

    /**
     * <p>Upload ID after which listing began.</p>
     */
    inline ListMultipartUploadsResult& WithUploadIdMarker(const Aws::String& value) { SetUploadIdMarker(value); return *this;}

    /**
     * <p>Upload ID after which listing began.</p>
     */
    inline ListMultipartUploadsResult& WithUploadIdMarker(Aws::String&& value) { SetUploadIdMarker(std::move(value)); return *this;}

    /**
     * <p>Upload ID after which listing began.</p>
     */
    inline ListMultipartUploadsResult& WithUploadIdMarker(const char* value) { SetUploadIdMarker(value); return *this;}


    /**
     * <p>When a list is truncated, this element specifies the value that should be
     * used for the key-marker request parameter in a subsequent request.</p>
     */
    inline const Aws::String& GetNextKeyMarker() const{ return m_nextKeyMarker; }

    /**
     * <p>When a list is truncated, this element specifies the value that should be
     * used for the key-marker request parameter in a subsequent request.</p>
     */
    inline void SetNextKeyMarker(const Aws::String& value) { m_nextKeyMarker = value; }

    /**
     * <p>When a list is truncated, this element specifies the value that should be
     * used for the key-marker request parameter in a subsequent request.</p>
     */
    inline void SetNextKeyMarker(Aws::String&& value) { m_nextKeyMarker = std::move(value); }

    /**
     * <p>When a list is truncated, this element specifies the value that should be
     * used for the key-marker request parameter in a subsequent request.</p>
     */
    inline void SetNextKeyMarker(const char* value) { m_nextKeyMarker.assign(value); }

    /**
     * <p>When a list is truncated, this element specifies the value that should be
     * used for the key-marker request parameter in a subsequent request.</p>
     */
    inline ListMultipartUploadsResult& WithNextKeyMarker(const Aws::String& value) { SetNextKeyMarker(value); return *this;}

    /**
     * <p>When a list is truncated, this element specifies the value that should be
     * used for the key-marker request parameter in a subsequent request.</p>
     */
    inline ListMultipartUploadsResult& WithNextKeyMarker(Aws::String&& value) { SetNextKeyMarker(std::move(value)); return *this;}

    /**
     * <p>When a list is truncated, this element specifies the value that should be
     * used for the key-marker request parameter in a subsequent request.</p>
     */
    inline ListMultipartUploadsResult& WithNextKeyMarker(const char* value) { SetNextKeyMarker(value); return *this;}


    /**
     * <p>When a prefix is provided in the request, this field contains the specified
     * prefix. The result contains only keys starting with the specified prefix.</p>
     */
    inline const Aws::String& GetPrefix() const{ return m_prefix; }

    /**
     * <p>When a prefix is provided in the request, this field contains the specified
     * prefix. The result contains only keys starting with the specified prefix.</p>
     */
    inline void SetPrefix(const Aws::String& value) { m_prefix = value; }

    /**
     * <p>When a prefix is provided in the request, this field contains the specified
     * prefix. The result contains only keys starting with the specified prefix.</p>
     */
    inline void SetPrefix(Aws::String&& value) { m_prefix = std::move(value); }

    /**
     * <p>When a prefix is provided in the request, this field contains the specified
     * prefix. The result contains only keys starting with the specified prefix.</p>
     */
    inline void SetPrefix(const char* value) { m_prefix.assign(value); }

    /**
     * <p>When a prefix is provided in the request, this field contains the specified
     * prefix. The result contains only keys starting with the specified prefix.</p>
     */
    inline ListMultipartUploadsResult& WithPrefix(const Aws::String& value) { SetPrefix(value); return *this;}

    /**
     * <p>When a prefix is provided in the request, this field contains the specified
     * prefix. The result contains only keys starting with the specified prefix.</p>
     */
    inline ListMultipartUploadsResult& WithPrefix(Aws::String&& value) { SetPrefix(std::move(value)); return *this;}

    /**
     * <p>When a prefix is provided in the request, this field contains the specified
     * prefix. The result contains only keys starting with the specified prefix.</p>
     */
    inline ListMultipartUploadsResult& WithPrefix(const char* value) { SetPrefix(value); return *this;}


    
    inline const Aws::String& GetDelimiter() const{ return m_delimiter; }

    
    inline void SetDelimiter(const Aws::String& value) { m_delimiter = value; }

    
    inline void SetDelimiter(Aws::String&& value) { m_delimiter = std::move(value); }

    
    inline void SetDelimiter(const char* value) { m_delimiter.assign(value); }

    
    inline ListMultipartUploadsResult& WithDelimiter(const Aws::String& value) { SetDelimiter(value); return *this;}

    
    inline ListMultipartUploadsResult& WithDelimiter(Aws::String&& value) { SetDelimiter(std::move(value)); return *this;}

    
    inline ListMultipartUploadsResult& WithDelimiter(const char* value) { SetDelimiter(value); return *this;}


    /**
     * <p>When a list is truncated, this element specifies the value that should be
     * used for the upload-id-marker request parameter in a subsequent request.</p>
     */
    inline const Aws::String& GetNextUploadIdMarker() const{ return m_nextUploadIdMarker; }

    /**
     * <p>When a list is truncated, this element specifies the value that should be
     * used for the upload-id-marker request parameter in a subsequent request.</p>
     */
    inline void SetNextUploadIdMarker(const Aws::String& value) { m_nextUploadIdMarker = value; }

    /**
     * <p>When a list is truncated, this element specifies the value that should be
     * used for the upload-id-marker request parameter in a subsequent request.</p>
     */
    inline void SetNextUploadIdMarker(Aws::String&& value) { m_nextUploadIdMarker = std::move(value); }

    /**
     * <p>When a list is truncated, this element specifies the value that should be
     * used for the upload-id-marker request parameter in a subsequent request.</p>
     */
    inline void SetNextUploadIdMarker(const char* value) { m_nextUploadIdMarker.assign(value); }

    /**
     * <p>When a list is truncated, this element specifies the value that should be
     * used for the upload-id-marker request parameter in a subsequent request.</p>
     */
    inline ListMultipartUploadsResult& WithNextUploadIdMarker(const Aws::String& value) { SetNextUploadIdMarker(value); return *this;}

    /**
     * <p>When a list is truncated, this element specifies the value that should be
     * used for the upload-id-marker request parameter in a subsequent request.</p>
     */
    inline ListMultipartUploadsResult& WithNextUploadIdMarker(Aws::String&& value) { SetNextUploadIdMarker(std::move(value)); return *this;}

    /**
     * <p>When a list is truncated, this element specifies the value that should be
     * used for the upload-id-marker request parameter in a subsequent request.</p>
     */
    inline ListMultipartUploadsResult& WithNextUploadIdMarker(const char* value) { SetNextUploadIdMarker(value); return *this;}


    /**
     * <p>Maximum number of multipart uploads that could have been included in the
     * response.</p>
     */
    inline int GetMaxUploads() const{ return m_maxUploads; }

    /**
     * <p>Maximum number of multipart uploads that could have been included in the
     * response.</p>
     */
    inline void SetMaxUploads(int value) { m_maxUploads = value; }

    /**
     * <p>Maximum number of multipart uploads that could have been included in the
     * response.</p>
     */
    inline ListMultipartUploadsResult& WithMaxUploads(int value) { SetMaxUploads(value); return *this;}


    /**
     * <p>Indicates whether the returned list of multipart uploads is truncated. A
     * value of true indicates that the list was truncated. The list can be truncated
     * if the number of multipart uploads exceeds the limit allowed or specified by max
     * uploads.</p>
     */
    inline bool GetIsTruncated() const{ return m_isTruncated; }

    /**
     * <p>Indicates whether the returned list of multipart uploads is truncated. A
     * value of true indicates that the list was truncated. The list can be truncated
     * if the number of multipart uploads exceeds the limit allowed or specified by max
     * uploads.</p>
     */
    inline void SetIsTruncated(bool value) { m_isTruncated = value; }

    /**
     * <p>Indicates whether the returned list of multipart uploads is truncated. A
     * value of true indicates that the list was truncated. The list can be truncated
     * if the number of multipart uploads exceeds the limit allowed or specified by max
     * uploads.</p>
     */
    inline ListMultipartUploadsResult& WithIsTruncated(bool value) { SetIsTruncated(value); return *this;}


    
    inline const Aws::Vector<MultipartUpload>& GetUploads() const{ return m_uploads; }

    
    inline void SetUploads(const Aws::Vector<MultipartUpload>& value) { m_uploads = value; }

    
    inline void SetUploads(Aws::Vector<MultipartUpload>&& value) { m_uploads = std::move(value); }

    
    inline ListMultipartUploadsResult& WithUploads(const Aws::Vector<MultipartUpload>& value) { SetUploads(value); return *this;}

    
    inline ListMultipartUploadsResult& WithUploads(Aws::Vector<MultipartUpload>&& value) { SetUploads(std::move(value)); return *this;}

    
    inline ListMultipartUploadsResult& AddUploads(const MultipartUpload& value) { m_uploads.push_back(value); return *this; }

    
    inline ListMultipartUploadsResult& AddUploads(MultipartUpload&& value) { m_uploads.push_back(std::move(value)); return *this; }


    
    inline const Aws::Vector<CommonPrefix>& GetCommonPrefixes() const{ return m_commonPrefixes; }

    
    inline void SetCommonPrefixes(const Aws::Vector<CommonPrefix>& value) { m_commonPrefixes = value; }

    
    inline void SetCommonPrefixes(Aws::Vector<CommonPrefix>&& value) { m_commonPrefixes = std::move(value); }

    
    inline ListMultipartUploadsResult& WithCommonPrefixes(const Aws::Vector<CommonPrefix>& value) { SetCommonPrefixes(value); return *this;}

    
    inline ListMultipartUploadsResult& WithCommonPrefixes(Aws::Vector<CommonPrefix>&& value) { SetCommonPrefixes(std::move(value)); return *this;}

    
    inline ListMultipartUploadsResult& AddCommonPrefixes(const CommonPrefix& value) { m_commonPrefixes.push_back(value); return *this; }

    
    inline ListMultipartUploadsResult& AddCommonPrefixes(CommonPrefix&& value) { m_commonPrefixes.push_back(std::move(value)); return *this; }


    /**
     * <p>Encoding type used by Amazon S3 to encode object keys in the response.</p>
     */
    inline const EncodingType& GetEncodingType() const{ return m_encodingType; }

    /**
     * <p>Encoding type used by Amazon S3 to encode object keys in the response.</p>
     */
    inline void SetEncodingType(const EncodingType& value) { m_encodingType = value; }

    /**
     * <p>Encoding type used by Amazon S3 to encode object keys in the response.</p>
     */
    inline void SetEncodingType(EncodingType&& value) { m_encodingType = std::move(value); }

    /**
     * <p>Encoding type used by Amazon S3 to encode object keys in the response.</p>
     */
    inline ListMultipartUploadsResult& WithEncodingType(const EncodingType& value) { SetEncodingType(value); return *this;}

    /**
     * <p>Encoding type used by Amazon S3 to encode object keys in the response.</p>
     */
    inline ListMultipartUploadsResult& WithEncodingType(EncodingType&& value) { SetEncodingType(std::move(value)); return *this;}

  private:

    Aws::String m_bucket;

    Aws::String m_keyMarker;

    Aws::String m_uploadIdMarker;

    Aws::String m_nextKeyMarker;

    Aws::String m_prefix;

    Aws::String m_delimiter;

    Aws::String m_nextUploadIdMarker;

    int m_maxUploads;

    bool m_isTruncated;

    Aws::Vector<MultipartUpload> m_uploads;

    Aws::Vector<CommonPrefix> m_commonPrefixes;

    EncodingType m_encodingType;
  };

} // namespace Model
} // namespace S3
} // namespace Aws
