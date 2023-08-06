# marqeta-sdk-codegen
Tool to generate repetitive code using templates
```requirments```
npm install ejs 

```to generate marqeta-sdk-python ```

./cli.js --target python


``` To run drone locally ```
```Tokens are defined in environment variables```

    SDK_BASE_URL
    SDK_APP_TOKEN
    SDK_ACCESS_TOKEN
```and  to run ```
drone exec --event tag  --env-file ~/.<env_file> 

```link for builds on drone```
https://drone.marqeta.com/marqeta/marqeta-sdk-codegen