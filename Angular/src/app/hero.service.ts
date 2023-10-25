import {Injectable} from '@angular/core';
import {Hero} from "./heroes/hero/hero.model";
import {concatMap, delay, from, Observable, of} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class HeroService {
  mockHeroList: Array<Hero> = [
    new Hero(1, 'Batman', 10),
    new Hero(2, 'Pacman', 20),
    new Hero(3, 'Superman', 30),
    new Hero(4, 'SpiderMan', 90),
    new Hero(5, 'Ironman', 85),
  ]

  getAllHeroes(): Observable<Array<Hero>> {
    return of(this.mockHeroList).pipe(delay(2500));
  }

  rotateAllHeroes(): Observable<Hero> {
    return from(this.mockHeroList).pipe(
      concatMap(item => of(item).pipe(delay(1000))
      )
    );
  }

  constructor() {
  }
}
