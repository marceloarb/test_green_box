const devs = [
    {
        name: 'Cameron',
        age: 23,
        gender: 'm',
        "tech_stack" : ['html','css','js','React']
    },
    {
        name: 'Liz',
        age: 20,
        gender: 'f',
        "tech_stack" : ['java','spring-boot','MySql']
    },
    {
        name: 'Chris',
        age: 102,
        gender: 'm',
        "tech_stack" : ['react','express','python']
    },
    {
        name: 'Rashid',
        age: 27,
        gender: 'm',
        "tech_stack" : ['thymeleaf','postgres','js','Angular']
    },
    {
        name: 'Annie',
        age: 30,
        gender: 'F',
        "tech_stack" : ['html','scss','less','DynamoDB','GraphQL']
    },
    {
        name: 'Dr. Patel',
        age: 52,
        gender: 'M',
        "tech_stack" : null
    },
    {
        name: 'Isaiah',
        age: 48,
        gender: 'M',
        "tech_stack" : ['Java','','less','DynamoDB','GraphQL']
    },
    {
        name: 'Saima',
        age: 33,
        gender: 'F',
        "tech_stack" : ['MongoDB','Route53','Jenkins','Terraform','Kubernetes']
    },
    {
        name: 'Omar',
        age: 33,
        gender: 'm',
        "tech_stack" : ['c++']
    },
    {
        name: 'Mariam',
        age: 32,
        gender: 'f',
        "tech_stack" : null
    },
];

const result = devs.filter(dev => dev.tech_stack != null);
console.log(result);