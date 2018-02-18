$(document).ready(function () {
    $('.reg_form').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            //Aleatorios
            n: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',
                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 1,
                        max: 10000,
                        message: 'Debe ingresar un rango de 1 a 10000'
                    }

                }


            },
            a: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',
                        // The default separators

                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 1,
                        max: 10000,
                        message: 'Debe ingresar un rango de 1 a 10000'
                    }
                }


            },
            xo: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',
                        // The default separators

                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 1,
                        max: 10000,
                        message: 'Debe ingresar un rango de 1 a 10000'
                    }
                }


            },
            c: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',
                        // The default separators

                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 1,
                        max: 10000,
                        message: 'Debe ingresar un rango de 1 a 10000'
                    }
                }


            },
            m: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',
                        // The default separators

                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 1,
                        max: 10000,
                        message: 'Debe ingresar un rango de 1 a 10000'
                    }
                }


            },
            x: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',
                        // The default separators

                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 1,
                        max: 10000,
                        message: 'Debe ingresar un rango de 1 a 10000'
                    }
                }


            },
            d: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',
                        // The default separators

                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 1,
                        max: 10000,
                        message: 'Debe ingresar un rango de 1 a 10000'
                    }
                }


            },
            nb: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',
                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 1,
                        max: 10000,
                        message: 'Debe ingresar un rango de 1 a 10000'
                    }

                }


            },
            ab: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',


                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 1,
                        max: 10000,
                        message: 'Debe ingresar un rango de 1 a 10000'
                    }
                }


            },
            xob: {
                validators: {
                    integer: {
                        message: 'El valor no es un Entero',

                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 1,
                        max: 10000,
                        message: 'Debe ingresar un rango de 1 a 10000'
                    }
                }
            },
            cb: {
                validators: {
                    integer: {
                        message: 'El valor no es un Entero',

                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 1,
                        max: 10000,
                        message: 'Debe ingresar un rango de 1 a 10000'
                    }
                }


            },
            mb: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',
                        // The default separators
                        thousandsSeparator: '',
                        decimalSeparator: '.'
                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 1,
                        max: 10000,
                        message: 'Debe ingresar un rango de 1 a 10000'
                    }
                }


            },
            cnumeros: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',

                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 1,
                        max: 1000,
                        message: 'Debe ingresar un rango de 1 a 10000'
                    }
                }


            },

            //Linea de Espera

            vx: {

                validators: {

                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    }

                }
            },
            vfre: {

                validators: {
                    numeric: {
                        message: 'El valor no es un Entero',
                        // The default separators
                        thousandsSeparator: '',
                        decimalSeparator: '.'
                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 0.001,
                        max: 1,
                        message: 'Debe ingresar un rango mayor a 0 y menor que 1'
                    }
                }
            },
            txin: {

                validators: {
                    numeric: {
                        message: 'El valor no es un Entero',
                        // The default separators
                        thousandsSeparator: '',
                        decimalSeparator: '.'
                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 1,
                        max: 1,
                        message: 'Debe ingresar un rango mayor a 0 y menor que 1'
                    }
                }
            },
            riLlegadas: {

                validators: {
                    numeric: {
                        message: 'El valor no es un Entero',
                        // The default separators
                        thousandsSeparator: '',
                        decimalSeparator: '.'
                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 0.001,
                        max: 1,
                        message: 'Debe ingresar un rango mayor a 0 y menor que 1'
                    }
                }
            },
            riServicio: {

                validators: {
                    numeric: {
                        message: 'El valor no es un Entero',
                        // The default separators
                        thousandsSeparator: '',
                        decimalSeparator: '.'
                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 0.001,
                        max: 1,
                        message: 'Debe ingresar un rango mayor a 0 y menor que 1'
                    }
                }
            },
            //modelo Inventario
            valorDemanda: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',
                        // The default separators
                        thousandsSeparator: '',
                        decimalSeparator: '.'
                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 0.001,
                        max: 1,
                        message: 'Debe ingresar un rango mayor a 0 y menor que 1'
                    }
                }
            },
            valorRetraso: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',
                        // The default separators
                        thousandsSeparator: '',
                        decimalSeparator: '.'
                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 0.001,
                        max: 1,
                        message: 'Debe ingresar un rango mayor a 0 y menor que 1'
                    }
                }
            },

            //select metodo
            metodoa: {
                validators: {
                    notEmpty: {
                        message: 'Por Favor Seleccione un Método'
                    }
                }
            },

            //caso de estudio
            //Absoluta
            demandaLlegadasA: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',

                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 0,
                        max: 10000,
                        message: 'Debe ingresar un rango de 0 a 10000'
                    }
                }
            },
            valorLlegadasA: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',

                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 0,
                        max: 10000,
                        message: 'Debe ingresar un rango de 0 a 10000'
                    }
                }
            },
            demandaServicioA: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',

                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 0,
                        max: 10000,
                        message: 'Debe ingresar un rango de 0 a 10000'
                    }
                }
            },
            valorServicioA: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',

                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 0,
                        max: 10000,
                        message: 'Debe ingresar un rango de 0 a 10000'
                    }
                }
            },
            //Relativa
             demandaLlegadas: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero'

                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 0,
                        max: 10000,
                        message: 'Debe ingresar un rango de 0 a 10000'
                    }
                }


            },

            demandaServicio: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero'

                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 0,
                        max: 10000,
                        message: 'Debe ingresar un rango de 0 a 10000'
                    }
                }


            },

            last_name: {
                validators: {
                    stringLength: {
                        min: 2
                    },
                    notEmpty: {
                        message: 'Please supply your last name'
                    }
                }
            },
            valorLlegadas: {

                validators: {
                    numeric: {
                        message: 'El valor no es un Entero',
                        // The default separators
                        thousandsSeparator: '',
                        decimalSeparator: '.'
                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 0,
                        max: 1,
                        message: 'aDebe ingresar un rango mayor a 0 y menor que 1'
                    }
                }
            },
            valorServicio: {

                validators: {
                    numeric: {
                        message: 'El valor no es un Entero',
                        // The default separators
                        thousandsSeparator: '',
                        decimalSeparator: '.'
                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 0,
                        max: 1,
                        message: 'Debe ingresar un rango mayor a 0 y menor que 1'
                    }
                }
            },
///////////
            phone: {
                validators: {
                    notEmpty: {
                        message: 'Please supply your phone number'
                    },
                    phone: {
                        country: 'US',
                        message: 'Please supply a vaild phone number with area code'
                    }
                }
            },
            address: {
                validators: {
                    stringLength: {
                        min: 8,
                    },
                    notEmpty: {
                        message: 'Please supply your street address'
                    }
                }
            },
            city: {
                validators: {
                    stringLength: {
                        min: 4,
                    },
                    notEmpty: {
                        message: 'Please supply your city'
                    }
                }
            },
            state: {
                validators: {
                    notEmpty: {
                        message: 'Please select your state'
                    }
                }
            },
            zip: {
                validators: {
                    notEmpty: {
                        message: 'Please supply your zip code'
                    },
                    zipCode: {
                        country: 'US',
                        message: 'Please supply a vaild zip code'
                    }
                }
            },
            comment: {
                validators: {
                    stringLength: {
                        min: 10,
                        max: 200,
                        message: 'Please enter at least 10 characters and no more than 200'
                    },
                    notEmpty: {
                        message: 'Please supply a description about yourself'
                    }
                }
            },
            email: {
                validators: {
                    notEmpty: {
                        message: 'Please supply your email address'
                    },
                    emailAddress: {
                        message: 'Please supply a valid email address'
                    }
                }
            },

            password: {
                validators: {
                    identical: {
                        field: 'confirmPassword',
                        message: 'Confirm your password below - type same password please'
                    }
                }
            },
            confirmPassword: {
                validators: {
                    identical: {
                        field: 'password',
                        message: 'The password and its confirm are not the same'
                    }
                }
            }


        }
    })

    $('.num_form').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {

            nLlegadas: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',
                        // The default separators
                        thousandsSeparator: '',
                        decimalSeparator: '.'
                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 1,
                        max: 10000,
                        message: 'Debe ingresar un rango de 1 a 10000'
                    }
                }
            },
            nServicio: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',
                        // The default separators
                        thousandsSeparator: '',
                        decimalSeparator: '.'
                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 1,
                        max: 10000,
                        message: 'Debe ingresar un rango de 1 a 10000'
                    }
                }
            },
            nDemanda: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',
                        // The default separators
                        thousandsSeparator: '',
                        decimalSeparator: '.'
                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 1,
                        max: 10000,
                        message: 'Debe ingresar un rango de 1 a 10000'
                    }
                }
            },
            nRetraso: {

                validators: {
                    integer: {
                        message: 'El valor no es un Entero',
                        // The default separators
                        thousandsSeparator: '',
                        decimalSeparator: '.'
                    },
                    notEmpty: {
                        message: 'Por favor ingrese un Valor'
                    },
                    between: {
                        min: 1,
                        max: 10000,
                        message: 'Debe ingresar un rango de 1 a 10000'
                    }
                }
            }


        }
    })

        .on('success.form.bv', function (e) {
            $('#success_message').slideDown({opacity: "show"}, "slow") // Do something ...
            $('#reg_form').data('bootstrapValidator').resetForm();

            // Prevent form submission
            e.preventDefault();

            // Get the form instance
            var $form = $(e.target);

            // Get the BootstrapValidator instance
            var bv = $form.data('bootstrapValidator');

            // Use Ajax to submit form data
            $.post($form.attr('action'), $form.serialize(), function (result) {
                console.log(result);
            }, 'json');
        });

});

