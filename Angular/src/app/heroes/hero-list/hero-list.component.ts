import {Component, OnInit} from '@angular/core';
import {Hero} from '../hero/hero.model';
import {formatDate} from '@angular/common';
import {HeroService} from "../../hero.service";

@Component({
  selector: 'app-hero-list',
  templateUrl: './hero-list.component.html',
  styleUrls: ['./hero-list.component.css']
})
export class HeroListComponent implements OnInit {

  private _title: string = 'I ♥ Angular';
  count: number = 0;
  currentDate: Date = new Date();
  isDisplayed: boolean = false;
  isSpecial: boolean;
  heroArray: Array<Hero> = new Array<Hero>();
  currentHero: Hero | undefined;
  heroesList: Array<Hero> | undefined;

  constructor(private heroService: HeroService) {
    this.isSpecial = false;
  }

  get title(): string {
    return this._title;
  }

  set title(val: string) {

    this._title = val;
  }

  ngOnInit(): void {

    this.heroService.getAllHeroes().subscribe(resHeroList => {
      this.heroesList = resHeroList;

      if (this.heroesList.length > 0) {
        this.currentHero = this.heroesList.at(0);
      }
    });


    setInterval(() => {
      this.currentDate = new Date();
    }, 1000);


    this.heroArray.push(new Hero(1, 'Batman', 80));
    this.heroArray.push(new Hero(2, 'Superman', 30));
    this.heroArray.push(new Hero(3, 'Pacman', 100))

  }

  onButtonClicked(event: Event, nbToAdd: number) {
    this.count += nbToAdd;
  }

  rotateHeroClicked() {
    this.heroService.rotateAllHeroes().subscribe(hero => {
      this.currentHero = hero;
      this.isSpecial = this.currentHero.name === 'SpiderMan';
    })
  }

}

function newHero(arg0: string, arg1: number): Hero {
  throw new Error('Function not implemented.');
}

