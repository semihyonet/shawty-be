from app.core.services.AppDao import AppDAO


class CounterDAO(AppDAO):
    def get_counter(self, counter_name: str, default_value: int) -> int:
        counter_collection = self.db["CounterModel"]
        filter_query = {'name': counter_name}  # Replace 'counterId' with the actual document identifier
        update_operation = {'$inc': {'counter': 1}}  # Increment the 'counter' field by 1

        a = counter_collection.find_one_and_update(
            filter_query,
            update_operation,
            return_document=True,  # Return the document after the update
            upsert=True,  # Create the document if it doesn't exist
        )

        if a['counter'] == 1: # This is the first time the counter is being incremented
            counter_collection.update_one(
                filter_query,
                {'$set': {'counter': default_value}}
            )
            return default_value

        return a['counter']
