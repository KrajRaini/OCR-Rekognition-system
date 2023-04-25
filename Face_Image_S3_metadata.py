import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('1.jpg','APJ Kalam'),
      ('2.jpg','CV Raman'),
      ('3.jpg','Albert Einstein'),
      ('4.jpg','Isaac Newton'),
      ('5.jpg','Nikola Tesla')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('face1collectionbucket','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]}
                    )