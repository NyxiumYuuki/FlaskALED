import { TestBed } from '@angular/core/testing';

import { HashageService } from './hashage.service';

describe('HashageService', () => {
  let service: HashageService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(HashageService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
