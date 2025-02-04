# Use official Node.js image
FROM node:18

# Set working directory inside the container
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Copy the rest of the files
COPY . .

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["node", "app.js"]
