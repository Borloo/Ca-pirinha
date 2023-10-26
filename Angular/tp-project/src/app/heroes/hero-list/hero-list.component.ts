import { Component, OnInit } from '@angular/core';
import { Hero } from '../hero/hero.model';
import { formatDate } from '@angular/common';
import {HeroListService} from "./hero-list.service";
import {Observable} from "rxjs";

@Component({
  selector: 'app-hero-list',
  templateUrl: './hero-list.component.html',
  styleUrls: ['./hero-list.component.css']
})
export class HeroListComponent implements OnInit {

  private _title: string = 'I ♥Angular';
  count: number = 0;
  currentDate: Date = new Date();
  isDisplayed: boolean = false;
  heroArray: Array<Hero>|undefined;
  currentHero: Hero|undefined

  get title(): string {
    return this._title;
  }

  set title(val: string) {

    this._title = val;
  }

  constructor(private heroListService: HeroListService) { }

  ngOnInit(): void {
    // setTimeout(() => {
    //   this.isDisplayed = true
    // }, 5000);

    setInterval(() => {
      this.currentDate = new Date();
    }, 1000);


    this.heroListService.getAllHeroes().subscribe(resHeroList => {
      this.heroArray = resHeroList
      if(this.heroArray.length> 0) {
        this.currentHero= this.heroArray.at(0);
      }
    })

  }

  rotateHeroClicked() {
    this.heroListService.rotateAllHeroes().subscribe(hero=>{this.currentHero= hero;})
  }

  onButtonClicked(event: Event, nbToAdd: number) {
    this.count += nbToAdd;
  }

}

function newHero(arg0: string, arg1: number): Hero {
  throw new Error('Function not implemented.');
}

