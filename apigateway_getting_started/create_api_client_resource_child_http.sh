aws apigateway put-integration --rest-api-id abcd1234 \
  --resource-id bbb222 --http-method GET --type HTTP \
  --integration-http-method GET \
  --uri 'http://petstore-demo-endpoint.execute-api.com/petstore/pets/{id}' \ 
  --request-parameters '{"integration.request.path.id":"method.request.path.petId"}' \
  --region us-west-2