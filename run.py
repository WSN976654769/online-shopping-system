from routes import app, warehouse, user_db


if __name__ == '__main__':
    # SIGINT to stop (Ctrl + C)
    app.run(debug=True)

    # Saves the data
    print('Saving...')
    warehouse.save_data()
    user_db.save_data()
    print('Save complete')