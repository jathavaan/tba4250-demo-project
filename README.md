# TBA4250 GIB 2 Template project

> [!NOTE]
> This is a template project that configures a React + Vite frontend, Python FastAPI backend with a PostgreSQL database.
> The project can be used as a template for the project in TBA4250 GIB 2.

### Setup

There is a [`docker-compose.yml`](./docker-compose.yml) in the root directory of the project. Files related to the
frontend can be found in the [client](./client)-directory, and the backend source code is in the [server](./server)
-directory.

#### Environment files

We will use env-files to ensure that secrets are not published. These files are ignored in the [
`.gitignore`](./.gitignore). The directories `client` and `server` will have one env-file each. Both these files have to
be named `.env`. developer have to create this as this defines the local credentials on their computer.

`server/.env` contains database connection credentials and looks something like this.

```.dotenv
POSTGRES_DB=templatedb
POSTGRES_USER=app
POSTGRES_PASSWORD=my-secret-password-123
```

These credentials can and should be changed to something secure. The `client/.env` only really holds the backend base
URL.

```dotenv
VITE_BACKEND_BASE_URL=http://localhost:5000
```

To be able to access environment variables in a Vite app all variables have to be prefixed with `VITE_` in the env-file.

BOM is a common cause for bugs when working with YAML- and env-files, and it is therefore important to remove it before
building Docker images.

#### Running the project

Whilst in the root directory run `docker-compose up -d` in the terminal. This will start all containers defined in the
`docker-compose` file. This assumes that Docker has been installed and configured on the computer.