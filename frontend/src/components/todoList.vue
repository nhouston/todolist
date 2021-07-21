<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Items on my todo list</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.item-modal>Add item</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Complete?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in list" :key="index">
              <td>{{ item.title }}</td>
              <td>
                <span v-if="item.complete">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.item-update-modal
                          @click="editItem(item)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteItem(item)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addItemModal"
            id="item-modal"
            title="Add a new list item"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Title:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addItemForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-complete-group">
          <b-form-checkbox-group v-model="addItemForm.complete" id="form-checks">
            <b-form-checkbox value="true">complete?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editItemModal"
            id="item-update-modal"
            title="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-title-edit-group"
                    label="Title:"
                    label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-complete-edit-group">
          <b-form-checkbox-group v-model="editForm.complete" id="form-checks">
            <b-form-checkbox value="true">complete?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      list: [],
      addItemForm: {
        title: '',
        complete: [],
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        title: '',
        complete: [],
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getItems() {
      const path = 'http://localhost:5000/items';
      axios.get(path)
        .then((res) => {
          this.list = res.data.list;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addItem(payload) {
      const path = 'http://localhost:5000/items';
      axios.post(path, payload)
        .then(() => {
          this.getItems();
          this.message = 'Todo item added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getItems();
        });
    },
    initForm() {
      this.addItemForm.title = '';
      this.addItemForm.complete = [];
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.complete = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addItemModal.hide();
      let complete = false;
      if (this.addItemForm.complete[0]) complete = true;
      const payload = {
        title: this.addItemForm.title,
        complete,
      };
      this.addItem(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addItemModal.hide();
      this.initForm();
    },
    editItem(item) {
      this.editForm = item;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editItemModal.hide();
      let complete = false;
      if (this.editForm.complete[0]) complete = true;
      const payload = {
        title: this.editForm.title,
        complete,
      };
      this.updateItem(payload, this.editForm.id);
    },
    updateItem(payload, itemID) {
      const path = `http://localhost:5000/items/${itemID}`;
      axios.put(path, payload)
        .then(() => {
          this.getItems();
          this.message = 'Todo list updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getItems();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editItemModal.hide();
      this.initForm();
      this.getItems();
    },
    removeItem(itemID) {
      const path = `http://localhost:5000/items/${itemID}`;
      axios.delete(path)
        .then(() => {
          this.getItems();
          this.message = 'List item removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getItems();
        });
    },
    onDeleteItem(item) {
      this.removeItem(item.id);
    },
  },
  created() {
    this.getItems();
  },
};
</script>
