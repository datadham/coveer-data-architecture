# API Documentation

This API provides endpoints for managing companies, campaigns, creators, participations, followers, and users. Each entity has endpoints to handle CRUD (Create, Read, Update, Delete) operations.

## Company API

### Create a Company
- **POST** `/companies`
  - Description: Create a new company record.

### Get Company
- **GET** `/companies/{company_id}`
  - Description: Retrieve a specific company by `company_id`.

### Update Company
- **PUT** `/companies/{company_id}`
  - Description: Update an existing company record.

### Delete Company
- **DELETE** `/companies/{company_id}`
  - Description: Remove a company record.

### List Companies
- **GET** `/companies`
  - Description: Retrieve all companies.

## Campaign API

### Create a Campaign
- **POST** `/campaigns`
  - Description: Create a new campaign record.

### Get Campaign
- **GET** `/campaigns/{campaign_id}`
  - Description: Retrieve a specific campaign by `campaign_id`.

### Update Campaign
- **PUT** `/campaigns/{campaign_id}`
  - Description: Update an existing campaign record.

### Delete Campaign
- **DELETE** `/campaigns/{campaign_id}`
  - Description: Remove a campaign record.

### List Campaigns by Company
- **GET** `/companies/{company_id}/campaigns`
  - Description: Retrieve all campaigns for a specific company.

## Creator API

### Create a Creator
- **POST** `/creators`
  - Description: Create a new creator record.

### Get Creator
- **GET** `/creators/{creator_id}`
  - Description: Retrieve a specific creator by `creator_id`.

### Update Creator
- **PUT** `/creators/{creator_id}`
  - Description: Update an existing creator record.

### Delete Creator
- **DELETE** `/creators/{creator_id}`
  - Description: Remove a creator record.

### List Creators
- **GET** `/creators`
  - Description: Retrieve all creators.

## Participation API

### Create Participation
- **POST** `/participations`
  - Description: Create a new participation record.

### Get Participation
- **GET** `/participations/{participation_id}`
  - Description: Retrieve a specific participation by `participation_id`.

### Update Participation
- **PUT** `/participations/{participation_id}`
  - Description: Update an existing participation record.

### Delete Participation
- **DELETE** `/participations/{participation_id}`
  - Description: Remove a participation record.

## User API

### Create User
- **POST** `/users`
  - Description: Create a new user record.

### Get User
- **GET** `/users/{user_id}`
  - Description: Retrieve a specific user by `user_id`.

### Update User
- **PUT** `/users/{user_id}`
  - Description: Update an existing user record.

### Delete User
- **DELETE** `/users/{user_id}`
  - Description: Remove a user record.

### List Users
- **GET** `/users`
  - Description: Retrieve all users.

## Authentication and Authorization

### Authenticate User
- **POST** `/auth/login`
  - Description: Authenticate a user and return a token.

### Register User
- **POST** `/auth/register`
  - Description: Register a new user.

### Password Reset
- **POST** `/auth/password-reset`
  - Description: Initiate a password reset process.
