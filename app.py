
import streamlit as st
import os
from auth_utils import login, is_authenticated
from crypto_utils import generate_aes_key, encrypt_message, decrypt_message, save_key, load_key
from log_utils import save_log

st.set_page_config(page_title="NeuroCrypt", layout="centered")

def main():
    st.title("🔐 NeuroCrypt - AI Powered Encryption")

    if not is_authenticated():
        login()
        return

    st.sidebar.title("📁 Options")
    option = st.sidebar.radio("Choose an action:", ("Encrypt Message", "Decrypt Message", "Upload File", "Download File", "Export Key"))

    if option == "Encrypt Message":
        plaintext = st.text_area("Enter your message to encrypt:")
        if st.button("Encrypt"):
            key = generate_aes_key()
            ciphertext = encrypt_message(plaintext, key)

            st.text_area("Encrypted Message", ciphertext, height=150)
            save_key(key)
            save_log("Encrypted a message")

            encrypted_bytes = ciphertext.encode()
            st.download_button(
                label="Download Encrypted Message",
                data=encrypted_bytes,
                file_name="encrypted_message.txt",
                mime="text/plain"
            )

            st.success("Message encrypted successfully and ready for download.")

    elif option == "Decrypt Message":
        ciphertext = st.text_area("Paste the encrypted message:")
        if st.button("Decrypt"):
            key = load_key()
            if key:
                plaintext = decrypt_message(ciphertext, key)
                st.text_area("Decrypted Message", plaintext, height=150)
                save_log("Decrypted a message")
                st.success("Message decrypted successfully.")
            else:
                st.error("No AES key found. Encrypt a message first or upload a key.")

    elif option == "Upload File":
        uploaded_file = st.file_uploader("Upload an encrypted file", type=["txt", "enc"])
        if uploaded_file is not None:
            os.makedirs("uploads", exist_ok=True)
            path = os.path.join("uploads", uploaded_file.name)
            content = uploaded_file.read()

            with open(path, "wb") as f:
                f.write(content)

            st.success(f"File {uploaded_file.name} uploaded successfully.")
            save_log(f"Uploaded file: {uploaded_file.name}")

            st.text_area("File Preview", content.decode(errors="ignore"), height=150)

            if st.button("Decrypt This File Now"):
                key = load_key()
                if key:
                    try:
                        decrypted = decrypt_message(content.decode(), key)
                        st.text_area("Decrypted Message", decrypted, height=150)
                        save_log(f"Decrypted uploaded file: {uploaded_file.name}")
                    except Exception:
                        st.error("Decryption failed. Check if the file content is valid or the key matches.")
                else:
                    st.error("No AES key found. Please export or upload a key first.")

    elif option == "Download File":
        os.makedirs("uploads", exist_ok=True)
        files = os.listdir("uploads")
        if files:
            file_to_download = st.selectbox("Select a file to download", files)
            with open(os.path.join("uploads", file_to_download), "rb") as f:
                st.download_button("Download", f.read(), file_name=file_to_download)
            save_log(f"Downloaded file: {file_to_download}")
        else:
            st.info("No files available to download.")

    elif option == "Export Key":
        key = load_key()
        if key:
            st.download_button("Download AES Key", key, file_name="aes_key.key")
            save_log("Exported AES key")
        else:
            st.error("No AES key available to export.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(f"App crashed: {e}")
