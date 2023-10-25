import { Component } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators }
  from '@angular/forms';
import { LimitedName } from './name.validator';

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrls: ['./test.component.css']
})
export class TestComponent {

  profileForm = this.fb.group({
    firstName: ['', [Validators.required,
    Validators.minLength(4), LimitedName(/bob/i)]],
    lastName: ['', [Validators.required,
    Validators.minLength(4), LimitedName(/bob/i)]],
    address: this.fb.group({
      street: [''],
      city: [''],
      zip: ['']
    }),
  });

  data: { firstName: string | null, lastName: string | null } =
    {
      firstName: 'Devienne-Ousmer',
      lastName: 'Julien',
    }

  address: { street: string | null, city: string | null, zip: string | null } = {
    street: '3 Imp. des champs',
    city: 'Toulouse',
    zip: '31000',
  }

  constructor(private fb: FormBuilder) { }

  ngOnInit() {
    this.profileForm.patchValue(this.data);
    this.profileForm.get('address')!.patchValue(this.address);
  }

  onSubmit() {
    if (this.profileForm.valid) {
      // Récupérer les valeurs du formulaire avec l'opérateur spread
      const formData = { ...this.profileForm.value };
      const addressData = { ...this.profileForm.get('address')!.value };

      // Afficher les données dans la console
      console.log('Données du formulaire principal :', formData);
      console.log('Données de l\'adresse :', addressData);
    }
  }

}
function newFormControl(arg0: any) {
  throw new Error('Function not implemented.');
}

function newFormGroup(arg0: { firstName: void; lastName: void; address: any; }) {
  throw new Error('Function not implemented.');
}

