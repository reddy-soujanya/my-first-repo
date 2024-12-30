for i in {1..5}
do
  echo "Calling GET API - Attempt $i"
  curl --location --request GET 'http://127.0.0.1:5000/users'
  echo # Add a newline for better readability between responses
done
