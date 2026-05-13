from app.services.vector_store import create_vector_store


def main():
    print("🔄 Creating FAISS index...")

    try:
        create_vector_store()
        print("✅ FAISS index created successfully!")
    except Exception as e:
        print("❌ Error while creating FAISS index:")
        print(str(e))


if __name__ == "__main__":
    main()