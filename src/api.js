const BASE_URL = "https://api.example.com";

async function fetchUser(userId) {
  const response = await fetch(`${BASE_URL}/users/${userId}`);
  if (!response.ok) throw new Error(`Failed to fetch user: ${response.status}`);
  return response.json();
}

async function createPost(title, body, authorId) {
  const response = await fetch(`${BASE_URL}/posts`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, body, authorId }),
  });
  if (!response.ok) throw new Error(`Failed to create post: ${response.status}`);
  return response.json();
}

module.exports = { fetchUser, createPost };
