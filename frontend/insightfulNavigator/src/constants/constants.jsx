import pg from 'pg'

export const dbConfig=new pg.Client({
    user:process.env.DB,
    password:process.env.DB_PASSWORD,
    host:process.env.DB_HOSTNAME,
    port:process.env.DB_PORT,
    database:process.env.DB_NAME
});

export const baseURL="http://localhost:5000/";

