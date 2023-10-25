import { Component, OnInit, numberAttribute } from '@angular/core';
import { Voiture } from '../model/hero.model';
import { formatDate } from '@angular/common';
import { FormBuilder, Validators } from '@angular/forms';


@Component({
  selector: 'app-hero-list',
  templateUrl: './hero-list.component.html',
  styleUrls: ['./hero-list.component.scss']
})
export class HeroListComponent implements OnInit {
      isDisplayed : boolean = false;
      name : string = "AHAHAH";
      voitures : Array<Voiture> = new Array<Voiture>();
      count : number = 0;
      date: Date = new Date();
      private _titre : string = "TITREEEEEE"; 
      data : { marque: string, modele: string, annee: string} =
      {marque: 'Citroen', modele: 'C3', annee: '2005'};
      voitureForm = this.fb.group({
        marque: ['', Validators.required],
        modele: ['', Validators.required],
        annee: ['', Validators.required, Validators.minLength(2)]
      })

      get titre(): string{
        return this._titre;
      }

      set titre(val: string){

        this._titre = val;  
      }

      constructor(private fb: FormBuilder){ }

      ngOnInit(): void {

        this.voitureForm.patchValue(this.data);
        setInterval(() => {
          this.date = new Date();
        }, 1000);

          setTimeout(()=> {
            this.isDisplayed = true;
          }, 5000)
          this.voitureForm.get('annee')?.errors
          this.voitures.push(new Voiture("Peugeot", "106", '1998'));
          this.voitures.push(new Voiture("Renault", "T16 Turbo", '1980'));
          this.voitures.push(new Voiture("Lancia", "S4", '1980'));     
      }
      onButtonClicked(nbToAdd : number){
        this.count+= nbToAdd;
      }



}
