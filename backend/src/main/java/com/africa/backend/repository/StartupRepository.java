package com.africa.backend.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.africa.backend.entity.Startup;

public interface StartupRepository extends JpaRepository<Startup, Integer> {

}
