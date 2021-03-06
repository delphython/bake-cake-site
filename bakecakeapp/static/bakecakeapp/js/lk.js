Vue.createApp({
    components: {
        VForm: VeeValidate.Form,
        VField: VeeValidate.Field,
        ErrorMessage: VeeValidate.ErrorMessage,
    },
    data() {
        return {
            Edit: false,
            Name: 'Ирина',
            Phone: '8 909 000-00-00',
            Email: 'nyam@gmail.com',
            Schema: {
                name_format: (value) => {
                    const regex = /^[a-zA-Zа-яА-я]+$/
                    if (!value) {
                        return '⚠ Поле не может быть пустым';
                    }
                    if ( !regex.test(value)) {

                        return '⚠ Недопустимые символы в имени';
                    }
                    return true;
                },
                phone_format: (value) => {
                    const regex = /^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$/
                    if (!value) {
                        return '⚠ Поле не может быть пустым';
                    }
                    if ( !regex.test(value)) {

                        return '⚠ Формат телефона нарушен';
                    }
                    return true;
                },
                email_format: (value) => {
                    const regex = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i
                    if (!value) {
                        return '⚠ Поле не может быть пустым';
                    }
                    if ( !regex.test(value)) {

                        return '⚠ Формат почты нарушен';
                    }
                    return true;
                }
            }
        }
    },
    methods: {
        ApplyChanges() {
            this.Edit = false
            console.log(this.Name, this.Phone, this.Email)

            // const url = "/save_user/"
            //
            // let csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
            //
            // const headers = {
            //   'Accept': 'application/json',
            //   'Content-Type': 'application/json',
            //   // 'X-CSRFToken': csrfToken,
            // }
            //
            // let data = JSON.stringify({
            //     name: this.Name,
            //     phone: this.Phone,
            //     email: this.Email,
            // }, null ,2)
            //
            // axios.post(url, data, {headers: headers})
            //   .then((response) => {console.log(response.data);})
            //   .catch((error) => {console.log(error);});
        }
    }
}).mount('#LK')
