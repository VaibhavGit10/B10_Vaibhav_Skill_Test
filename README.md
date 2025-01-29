# MultiEnv Ticket Management System

A full-stack application using Flask for both frontend and backend services, demonstrating environment-specific ticket management.

## Project Structure

```
multienv/
├── docker-compose.yml
├── backend/
│   ├── dev/
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   ├── Dockerfile
│   │   └── .env
│   └── prod/
│       ├── app.py
│       ├── requirements.txt
│       ├── Dockerfile
│       └── .env
└── frontend/
    ├── app.py
    ├── requirements.txt
    ├── Dockerfile
    └── .env
```

## Environment Configuration

### Backend Development Environment (.env)
```
PORT=5001
MONGO_URI=your_dev_mongodb_uri
```

### Backend Production Environment (.env)
```
PORT=5002
MONGO_URI=your_prod_mongodb_uri
```

### Frontend Environment (.env)
```
PORT=5000
DEV_DB_URI=your_dev_mongodb_uri
PROD_DB_URI=your_prod_mongodb_uri
```


### Requirements
```
flask==2.0.1
flask-cors==3.0.10
python-dotenv==0.19.0
pymongo==3.12.0
requests==2.26.0
```



### Using Docker Compose
```bash
docker-compose up
```

## Accessing the Application

- Frontend: http://localhost:5000/
- Development Environment: http://localhost:5000/dev
- Production Environment: http://localhost:5000/prod



## Development Notes

1. Both frontend and backend are Flask applications
2. Frontend uses Jinja2 templates for rendering
3. Backend serves JSON API endpoints
4. Each environment (dev/prod) has its own:
   - MongoDB connection
   - Port configuration
   - Flask application
   - Docker container

## Security Considerations

- Never commit `.env` files to version control
- Use different MongoDB databases for dev and prod
- Implement proper authentication
- Use secure headers

Remember: This is a basic setup focused on demonstrating multi-environment configuration. For a production system, you'll need to add proper security measures, testing, and error handling.