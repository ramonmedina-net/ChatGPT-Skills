# Persistence Test Protocol

Use before expensive research when a new local/cloud persistence mechanism is introduced.

1. Create `persistence_test.txt` in the proposed durable location.
2. Write:
   - an offset-aware timestamp;
   - a cryptographically random nonce.
3. Compute SHA-256.
4. Reopen the file in the same execution context and verify the hash.
5. Start a fresh execution context with no reliance on prior conversation.
6. Locate the file from the durable store.
7. Read its contents and independently reproduce the SHA-256.
8. Confirm success before substantive research.

If step 5–7 fails, the storage mechanism has not demonstrated the continuity property required by this skill.
